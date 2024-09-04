@REM check if /dist/run_app.exe exists
@IF EXIST "%~dp0dist\run_app.exe" (
    @REM run /dist/run_app.exe
    "%~dp0dist\run_app.exe"
) ELSE (
    @REM run /dist/run_app.py
    @REM python "%~dp0dist\run_app.py"
    echo "run_app.exe does not exist"
)