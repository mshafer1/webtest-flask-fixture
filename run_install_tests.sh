set -e
echo Building . . .
source build_command
echo Finished Building.

echo.
echo.


pushd webtest_flask_fixture

source __installed_tests_/run_tests
