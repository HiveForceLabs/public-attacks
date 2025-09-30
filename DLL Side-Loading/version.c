        $CSource =@(
        #include <windows.h>
        __declspec(dllexport) void $ExportedFunction()
        {
            MessageBoxA(NULL, "DLL Side-Loading via rundll32.exe succeeded!", "DLL Side-Loading", MB_OK | MB_ICONINFORMATION);
        }
        BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
        {
            return TRUE;
        }
        )