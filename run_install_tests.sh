set -e
echo Building . . .
source build_command
echo Finished Building.

echo ""
echo "" 


pushd webtest_flask_fixture

echo Running tests . . .
source examples/run_tests
echo Finshed tests
