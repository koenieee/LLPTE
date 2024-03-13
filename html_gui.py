import asyncio
from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from nicegui import run, ui
from random import random
from contextlib import contextmanager
from data_importer import RimayData
from logger import ResearchLogger
from rimay_verification import Paska_tool, RimayDSL

from wrapper_calls import ask_different_prompts


#['Few-shot learning', 'Chain-of-thought', 'Role play']
translation_type = "Few-shot learning" #fsl, cot, rp


#
# Given some precondition
# When I do some action
# Then I expect some result

# Given - the beginning state of the scenario
# When - specific action that the user makes
# Then - the outcome of the action in “When”

#Actors: UserA, SystemA


# Given: UserA navigates to the login page
# When: UserA clicks on button
# Then: SystemA refreshes page 

current_result = 0
paska_tool = Paska_tool()
start_acceptance_criteria="""Given: UserA navigates to the login page
When: UserA clicks on button
Then: SystemA refreshes page 
"""

start_rimay_actors = """Actors: actor SystemA, actor SystemB, actor SystemC, actor UserX, actor UserA, actor UserC
Classes: class Instruction := description record, class Y
"""

start_rimay_text = """When SystemB receives an "email alert" from SystemA, SystemB must send an Instruction to SystemC.
"""

# When the SystemA receives a rejection message from SystemB, 
# Then it must transform it to the corresponding XML message type and sent it to the SystemC.
input_text = start_acceptance_criteria
rimay_text = start_rimay_text
rimay_actor_text = start_rimay_actors


current_logger = None

echart = None


def update():
    global echart
    echart.options['series'][0]['data'][0] = random()
    echart.update()


def generate_stats():
    global echart
    echart = ui.echart({
        'xAxis': {'type': 'value'},
        'yAxis': {'type': 'category', 'data': ['A', 'B'], 'inverse': True},
        'legend': {'textStyle': {'color': 'gray'}},
        'series': [
            {'type': 'bar', 'name': 'Alpha', 'data': [0.1, 0.2]},
            {'type': 'bar', 'name': 'Beta', 'data': [0.3, 0.4]},
        ],
    })

def set_input_text(text):
    global input_text
    input_text = text
    print("Input text was: " + input_text)

def set_rimay_actors(actors):
    global rimay_actor_text
    rimay_actor_text = actors


def set_rimay_text(text):
    global rimay_text
    rimay_text = text

async def start_getting_results(sender): 
    await start_rimay_dsl_verification(sender)
    await start_paska_verification(sender)
    #When everything is finished, remove logger.

    current_logger = None

def make_rimay_input_text():
    with ui.card():
        with ui.card_section().style('width: 800px'):
            ui.markdown("## Input Rimay")

            ui.textarea(label='Rimay Actors and definitions', placeholder='start typing', value=start_rimay_actors,
                        on_change=lambda e: set_rimay_actors(e.value))
            ui.separator()

            ui.textarea(label='Rimay text', placeholder='start typing', value=start_rimay_text,
                        on_change=lambda e: set_rimay_text(e.value))
            result = ui.label()
            ui.html("<br>")
            with ui.row():
                ui.button('Check Rimay Paska', on_click=lambda e: start_getting_results(e.sender))
                #ui.button('Check Rimay DSL', on_click=lambda e: start_rimay_dsl_verification(e.sender))
            ui.html("<br>")

            



def make_intro_text():
    global input_text
    ui.markdown('# Translate Gherkin to Rimay')
    ui.markdown("Uses different prompting techniques to translate Gherkin (Given When Then) into Rimay (CNL)")
    ui.markdown("The following prompt techniques will be used:")
    ui.markdown("* Few-shot learning")
    ui.markdown("* Chain-of-thought")
    ui.markdown("* Role-play")
    with ui.card():
        with ui.card_section().style('width: 1000px'):
            ui.markdown("## Input Gherkin")

            ui.textarea(label='Acceptance Criteria', placeholder='start typing',  value=start_acceptance_criteria,
                        on_change=lambda e: set_input_text(e.value))
            result = ui.label()

    

def translation_buttons():
     with ui.card():
        with ui.card_section().style('width: 1000px'):

            ui.markdown("### Translation technique")
            with ui.row():
                ui.radio(['Few-shot learning', 'Chain-of-thought', 'Role play'], value='Few-shot learning', on_change=show_translation_type).props('inline')
            ui.separator()
            ui.html("<br>")
            ui.button('Translate', on_click=lambda e: start_translation(e.sender))


def compare_translations():
    ui.markdown("#### Translation result")
    ui.markdown("Result of translation from LLM:")
    with ui.splitter() as splitter:

        with splitter.before:
            ui.markdown("#### Gherkin").classes('mr-40')
            ui.html(input_text.replace("\n", "<br>")).classes('font-mono w-70')
        with splitter.after:
            ui.markdown("#### Rimay").classes('ml-5')
            ui.label(rimay_text).classes('font-mono ml-5')



def rimay_dsl_result(response):
    ui.separator()
    ui.html("<br><br>")
    ui.markdown("#### Rimay DSL tooling output")
    ui.html("<br><br>")

    with ui.scroll_area().classes('w-150 h-150 border'):
        if response[0].strip() == "Code generation finished.":
            ui.markdown("Succes!").classes('font-mono w-70').tailwind('text-green-600')
        if response[1].strip() != "":
            ui.html(response[1].replace("\n", "<br>")).classes('font-mono w-70').tailwind('text-red-600')

    ui.separator()


def paska_tooling_result(response):
    ui.markdown("#### Paska tooling output")
    ui.html("<br>")
    ui.markdown('Paska output.').classes('mr-40')
    ui.separator()
    ui.html("<br>")
    ui.label(response).classes('font-mono w-70')
    rimay = RimayData()
    ui.html("<br>")
    ui.html("<br>")

    ui.separator()
    ui.html("<br>")
    
    #ui.label("\n".join())
    rimay_result = rimay.load()
    columns = []
    rows = []
    for paska_item in rimay_result[0]:
        single_col = {
            'name': paska_item,
            'label': paska_item,
            'field': paska_item,
            'sortable': True,
            'align': 'left'
        }
        columns.append(single_col)

    for paska_result in rimay_result[1:]:
        single_row = {}
        for dict_item in paska_result:
            single_row[dict_item] = paska_result[dict_item]
        
        rows.append(single_row)
 

    ui.table(columns=columns, rows=rows, row_key='name', title="Rimay identification").classes('font-mono').style('width: 800px')



def make_results(result):
    ui.markdown("### Result translation " + str(current_result))
    ui.markdown(result)


def make_stats():
    ui.markdown("### Total Statistics")
    generate_stats()
    ui.button('Update', on_click=update)



def show_translation_type(event: ValueChangeEventArguments):
    global translation_type
    name = type(event.sender).__name__
    ui.notify(f'Selected {event.value}')
    translation_type = event.value


@contextmanager
def disable(button: ui.button):
    button.disable()
    try:
        yield
    finally:
        button.enable()


def show_llm_results(response):
    global start_rimay_text
    global rimay_text
    start_rimay_text = response
    rimay_text = response
    compare_translations()
    ui.html("<br>")
    make_rimay_input_text()
    ui.html("<br>")

    ui.separator().props('inline color=red')



def show_rimay_results(response):
    paska_tooling_result(response)
    #rimay_dsl_result


async def start_translation(button: ui.button):
    global current_result
    global current_logger
    button.disable()
    ui.html("<br>")
    current_result += 1
    spinner = ui.spinner(size='lg', color='blue')
    current_logger = ResearchLogger(translation_type) #Vervalt bij nieuwe logger.
    pre_content = f"""
## Gherkin Input
{input_text.strip()}

    """
    current_logger.append_result(pre_content)

    response = await run.io_bound(ask_different_prompts, input_text.strip(), translation_type, current_logger)
    button.enable()
    spinner.delete()
    show_llm_results(response)

    await start_getting_results(button)
    

async def start_rimay_dsl_verification(button: ui.button):
    global current_result
    button.disable()
    ui.html("<br>")
    current_result += 1
    spinner = ui.spinner(size='lg', color='red')
    dsl = RimayDSL()
    response = await run.io_bound(dsl.check_rimay_comf_dsl, rimay_actor_text + rimay_text)
    dsl.write_log_output(current_logger)

    button.enable()
    spinner.delete()
    rimay_dsl_result(response)
    ui.html("<br>")


async def start_paska_verification(button: ui.button):
    global current_result
    button.disable()
    ui.html("<br>")
    current_result += 1
    spinner = ui.spinner(size='lg', color='blue')

    response = await run.io_bound(paska_tool.check_rimay_requirement, rimay_text.strip().replace("\n",""))
    paska_tool.write_log_output(current_logger)

    button.enable()
    spinner.delete()
    show_rimay_results(response)
    ui.html("<br>")


def setup_ui():

    make_intro_text()
    translation_buttons()

    #make_results()

