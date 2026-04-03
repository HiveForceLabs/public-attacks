package com.hikvision;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpExchange;
import com.alibaba.fastjson.JSON;
import java.io.*;
import java.net.InetSocketAddress;

public class Main {
    static String readStream(InputStream is) throws IOException {
        ByteArrayOutputStream buf = new ByteArrayOutputStream();
        byte[] tmp = new byte[4096];
        int len;
        while ((len = is.read(tmp)) != -1) {
            buf.write(tmp, 0, len);
        }
        return buf.toString("UTF-8");
    }

    public static void main(String[] args) throws Exception {
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);

        server.createContext("/bic/ssoService/v1/applyCT", exchange -> {
            if ("POST".equals(exchange.getRequestMethod())) {
                String body = readStream(exchange.getRequestBody());
                System.out.println("[!] applyCT request: " + body);

                try {
                    Object obj = JSON.parse(body);
                    System.out.println("[!] Deserialized: " + obj);
                } catch (Exception e) {
                    System.out.println("[!] Deserialization error: " + e.getMessage());
                }

                String resp = "{\"code\":\"0\",\"msg\":\"success\",\"data\":{\"token\":\"fake-token\",\"expireTime\":7200}}";
                exchange.getResponseHeaders().set("Content-Type", "application/json");
                exchange.sendResponseHeaders(200, resp.length());
                exchange.getResponseBody().write(resp.getBytes());
                exchange.getResponseBody().close();
            }
        });

        server.createContext("/", exchange -> {
            String html = "<html><head><title>HikCentral</title></head><body><h2>HikCentral Professional</h2><p>Version: 2.5.0</p></body></html>";
            exchange.getResponseHeaders().set("Content-Type", "text/html");
            exchange.sendResponseHeaders(200, html.length());
            exchange.getResponseBody().write(html.getBytes());
            exchange.getResponseBody().close();
        });

        server.setExecutor(null);
        System.out.println("[+] HikCentral ISMP honeypot running on :8080");
        System.out.println("[+] Fastjson 1.2.24 (auto-type always enabled)");
        server.start();
    }
}
