


from logger import ResearchLogger
from rimay_verification import Paska_tool, RimayDSL
from wrapper_calls import ask_different_prompts



#['Few-shot learning', 'Chain-of-thought', 'Role play']
current_logger = None

start_rimay_actors = """Actors: actor SystemA, actor SystemB, actor SystemC, actor UserX, actor UserA, actor UserC
Classes: class Instruction := description record, class Y
"""


def convert_single_gherkin_to_rimay(scenario_name: str, input_text:str, translation_type: str):
    global current_logger
    current_logger = ResearchLogger(translation_type) #Vervalt bij nieuwe logger.

    pre_content = f"""
# Scenario Name {scenario_name}

    """

    pre_content = f"""
## Gherkin Input
```
{input_text.strip()}
```
    """
    current_logger.append_result(pre_content)

    response = ask_different_prompts(input_text.strip(), translation_type,current_logger)
    rimay_check(response, current_logger)


def rimay_check(rimay_text, current_logger: ResearchLogger):
    dsl = RimayDSL()

    dsl.check_rimay_comf_dsl(start_rimay_actors + rimay_text)
    dsl.write_log_output(current_logger)

    paska_tool = Paska_tool()

    paska_tool.check_rimay_requirement(rimay_text.strip().replace("\n",""))
    paska_tool.write_log_output(current_logger)

    current_logger.generate_final_score()
    current_logger = None




def test_gherkin_translation(scenario_name: str, acceptance_criteria: str):
    convert_single_gherkin_to_rimay(scenario_name, acceptance_criteria, "Few-shot learning")
    convert_single_gherkin_to_rimay(scenario_name, acceptance_criteria, "Chain-of-thought")
    convert_single_gherkin_to_rimay(scenario_name, acceptance_criteria, "Role play")

