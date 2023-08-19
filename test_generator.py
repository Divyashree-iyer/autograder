import unittest
import os
import os.path
import subprocess32 as subprocess
from subprocess32 import PIPE
from gradescope_utils.autograder_utils.decorators import weight, visibility
import yaml

BASE_DIR = './test_data'


class TestMetaclass(type):
    """
    Generates exercises and checks them against test cases
    """
    def __new__(self, name, bases, attrs):
        data_dir = attrs['data_dir']
        attrs[self.test_name(data_dir)] = self.generate_test(data_dir)
        return super(TestMetaclass, self).__new__(self, name, bases, attrs)

    @classmethod
    def generate_test(self, dir_name):
        """ Returns a testcase for the given directory """

        def load_file(path):
            full_path = os.path.join(BASE_DIR, dir_name, path)
            if os.path.isfile(full_path):
                with open(full_path, 'rb') as f:
                    return f.read()
            return None

        # def load_settings():
        #     settings_yml = load_file('settings.yml')

        #     if settings_yml is not None:
        #         return yaml.safe_load(settings_yml) or {}
        #     else:
        #         return {}

        # settings = load_settings()

        def compare_output(student_output, expected_output):
            return student_output.strip() == expected_output.decode().strip()

        # @weight(settings.get('weight', 1))
        # @visibility(settings.get('visibility', 'visible'))

        def compile_and_run(self):
            """ 
            Exercise
            """
            # Get path to exercise file
            exercise_number = dir_name.split("_")[1]
            path = os.path.join(BASE_DIR, dir_name, dir_name +'.cpp')
            

            #Compile code
            compile_cmd = f"g++ -o {path[:-4]} {path}"
            compile_result = subprocess.run(compile_cmd, shell=True)

            #Check for Compilation error
            if compile_result.returncode != 0:  
                print(f"Exercise {exercise_number} - Compilation error")
                # Note to Graders - we can add reason for the compilation fail here
                self.assertEqual(compile_result.returncode, 0, 'Compilation error')
                return 
            
            
            executable_name = './'+path[:-4]  # Get the name without .cpp

            # Note to Graders - we can add a loop here for running the code against multiple test cases
            input_data = load_file('input.txt')
            
            # Run the compiled executable
            process = subprocess.Popen([executable_name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate(input=input_data) 
                

            stdout_str = stdout.decode()  # Decode stdout from bytes to string
            stderr_str = stderr.decode()  # Decode stderr from bytes to string
            
            # Check for runtime errors
            if process.returncode != 0:
                print(f"Exercise {exercise_number} - Compilation or runtime error:", stderr_str)
                self.assertEqual(process.returncode, 0, 'Compilation or runtime error')
                return

            # Read expected output
            expected_output = load_file('output.txt')

            # Compare student's output with expected output
            if compare_output(stdout_str, expected_output):
                print(f"Exercise {exercise_number} - Passed")
            else:
                print(f"Exercise {exercise_number} - Failed")
            
            self.assertEqual(expected_output.decode().strip(), stdout_str.strip())
                
        return compile_and_run

    @staticmethod
    def klass_name(dir_name):
        return 'Test{0}'.format(''.join([x.capitalize() for x in dir_name.split('_')]))

    @staticmethod
    def test_name(dir_name):
        return 'test_{0}'.format(dir_name)


def build_test_class(data_dir):
    klass = TestMetaclass(
        TestMetaclass.klass_name(data_dir),
        (unittest.TestCase,),
        {
            'data_dir': data_dir
        }
    )
    return klass


def find_data_directories():
    return filter(
        lambda x: os.path.isdir(os.path.join(BASE_DIR, x)),
        os.listdir(BASE_DIR)
    )
