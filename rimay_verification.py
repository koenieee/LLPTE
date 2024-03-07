import shutil
from subprocess import PIPE, Popen
import csv
import os
import uuid 


class Paska_tool():

    def __init__(self) -> None:
        self.worskpace_dir = "/home/koebuntu/LLPTE"
        self.base_dir =f"{self.worskpace_dir}/existing_research/paska"
        self.preproces_tool = f"{self.base_dir}/source/get-parsing-trees/get_cparsingtrees.py"
        self.java_tool = f"{self.base_dir}/smell_detector.jar"
        self.pos_tagger_file = f"{self.worskpace_dir}/english-left3words-distsim.tagger"

        self.output_folder = f"{self.worskpace_dir}/generated_data/"
        self.input_folder_req = f"{self.output_folder}/input_requirements/"
        self.output_folder_pre = f"{self.output_folder}/output_pre/"
        self.output_folder_smells = f"{self.output_folder}/output_smells/"


        self.__init_directories()

    def __init_directories(self):
        shutil.rmtree(self.output_folder)
        os.mkdir(self.output_folder) 
        os.mkdir(self.input_folder_req)
        os.mkdir(self.output_folder_pre)
        os.mkdir(self.output_folder_smells)

    def write_input_file(self, id: str, requirement: str):
        #"RQSVV.024";"If System-A has successfully performed all the validation rules, then System-A must set the state of the Settlement Request to 'Valid'."
        #- Input: A csv text file containing requirements. Each requirement should have the following fields separated by the separator ";":
        # - Requirement ID (String)  
        # - Requirement (String)

        # field names
        # Define the data to be written to the CSV file
        data = [
            [id, requirement]
        ]
        
        # name of csv file
        filename = self.input_folder_req+"generated_rimay.csv"

        # Write data to the CSV file with a pipe delimiter
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_ALL)
            csvwriter.writerows(data)

    def run_process(self, input_args: list) -> str:
        process = Popen(input_args, stdout=PIPE, stderr=PIPE) #["conda activate smell-detector"]+
        result = process.communicate()
        print("Result STDOUT: "+ result[0].decode('utf-8'))
        print("Result STDERR: "+ result[1].decode('utf-8'))
        return result[0].decode('utf-8')
        


    def preprocess_paska(self) -> str:
        all_args = ["python", self.preproces_tool, self.input_folder_req, self.output_folder_pre]
        return self.run_process(all_args)

    def start_paska_tool(self) -> str:
        all_args = ["java", "-jar", self.java_tool, self.output_folder_pre, self.output_folder_smells, self.pos_tagger_file]
        return self.run_process(all_args)


    def check_rimay_requirement(self, requirement: str):
        self.clear_all_requirements()
        #/home/koebuntu/LLPTE/generated_data/output_smells/generated_rimay.csv.csv.csv
        self.write_input_file(uuid.uuid4(), requirement)
        self.preprocess_paska()
        return self.start_paska_tool()


    def clear_all_requirements(self):
        self.__init_directories()



class RimayDSL():

    def __init__(self) -> None:
        self.java_exe = "/home/koebuntu/eclipse//plugins/org.eclipse.justj.openjdk.hotspot.jre.full.linux.x86_64_17.0.6.v20230204-1729/jre/bin/java"
        self.jar_exe = "/home/koebuntu/LLPTE/existing_research/dsl_rimay-master/rimay_validator_dsl.jar"
        self.test_rimay_file = "/home/koebuntu/LLPTE/generated_data/dsl_check.rimay"

    def write_input_file(self, rimay_requirement:str):
        f = open(self.test_rimay_file, "w")
        f.write(rimay_requirement)
        f.close()    

    def execute_tool(self):
        all_args = [self.java_exe, "-jar",  self.jar_exe, self.test_rimay_file]
        return self._run_java(all_args)
    
    def check_rimay_comf_dsl(self, rimay_requirement:str):
        self.write_input_file(rimay_requirement)
        return self.execute_tool()

    def _run_java(self, input_args:list):
        process = Popen(input_args, stdout=PIPE, stderr=PIPE) #["conda activate smell-detector"]+
        result = process.communicate()
        print("Result STDOUT: "+ result[0].decode('utf-8'))
        print("Result STDERR: "+ result[1].decode('utf-8'))

        return (result[0].decode('utf-8'), result[1].decode('utf-8'))
        
