#ifndef PY_SERVICE_API_H //include guard
#define PY_SERVICE_API_H
#define PY_SSIZE_T_CLEAN
#include <python.h>
#include <Windows.h>
#include <Tchar.h>
#define SERVICE_NAME  _T("My Sample Service")
VOID WINAPI ServiceMain(DWORD, LPTSTR*);
VOID WINAPI ServiceCtrlHandler(DWORD);
DWORD WINAPI ServiceWorkerThread(LPVOID);
PyObject* g_callback;
#endif