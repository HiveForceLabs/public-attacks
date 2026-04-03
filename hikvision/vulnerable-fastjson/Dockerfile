FROM eclipse-temurin:8-jdk-alpine

COPY fastjson-1.2.24.jar /usr/local/lib/fastjson.jar
COPY src/ /app/src/
WORKDIR /app

RUN javac -cp /usr/local/lib/fastjson.jar src/com/hikvision/Main.java && \
    jar cfe hikvision-application.jar com.hikvision.Main -C src .

EXPOSE 8080
CMD ["java", "-cp", "/usr/local/lib/fastjson.jar:/app/hikvision-application.jar", "com.hikvision.Main"]
