import asyncio
from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from nicegui import run, ui
from random import random
from contextlib import contextmanager
from data_importer import RimayData
from rimay_verification import Paska_tool

from wrapper_calls import ask_different_prompts


#['Few-shot learning', 'Chain-of-thought', 'Role play']
translation_type = "Few-shot learning" #fsl, cot, rp


current_result = 0
paska_tool = Paska_tool()
start_acceptance_criteria="""
Given: that the account is overdrawn
And: the card is valid
When: the customer requests the cash
Then: ensure the rejection message is displayed
And: ensure cash isn't dispensed
"""

start_rimay_text = """
When the System-A receives a rejection message from System-B, 
Then it must transform it to the corresponding XML message type and sent it to the System-C.
"""

input_text = start_acceptance_criteria
rimay_text = start_rimay_text

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

def set_rimay_text(text):
    global rimay_text
    rimay_text = text

def make_rimay_input_text():
    with ui.card():
        with ui.card_section().style('width: 800px'):
            ui.markdown("## Input Rimay")

            ui.textarea(label='Rimay text', placeholder='start typing', value=start_rimay_text,
                        on_change=lambda e: set_rimay_text(e.value))
            result = ui.label()
            ui.html("<br>")

            ui.button('Check Rimay', on_click=lambda e: start_rimay_verification(e.sender))



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
    ui.markdown("The following translation happend from Gherkin to Rimay:")
    with ui.splitter() as splitter:

        with splitter.before:
            ui.markdown("#### Gherkin").classes('mr-40')
            ui.label(input_text).classes('mr-40')
        with splitter.after:
            ui.markdown("#### Rimay").classes('ml-40')
            ui.label(rimay_text).classes('ml-40')


def paska_tooling_result(response):
    ui.markdown("#### Paska tooling output")
    ui.label('Paska tooing output.').classes('mr-40')
    ui.separator()
    ui.html("<br>")
    ui.label("The result was: " + response).classes('font-mono w-70')
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
    make_results(response)
    ui.html("<br>")
    compare_translations()
    ui.html("<br>")
    make_rimay_input_text()
    ui.html("<br>")

    ui.separator().props('inline color=red')



def show_rimay_results(response):
    paska_tooling_result(response)



async def start_translation(button: ui.button):
    global current_result
    button.disable()
    ui.html("<br>")
    current_result += 1
    spinner = ui.spinner(size='lg', color='blue')

    response = await run.io_bound(ask_different_prompts, input_text.strip().replace("\n",""), translation_type)
    button.enable()
    spinner.delete()
    show_llm_results(response)


async def start_rimay_verification(button: ui.button):
    global current_result
    button.disable()
    ui.html("<br>")
    current_result += 1
    spinner = ui.spinner(size='lg', color='blue')
    #paska_tool.check_rimay_requirement("When an order cancellation message is received from the System-A then Reason must be displayed in the Sytem-B GUI field 'Reason of Cancellation'.")
    response = await run.io_bound(paska_tool.check_rimay_requirement, rimay_text.strip().replace("\n",""))
    button.enable()
    spinner.delete()
    show_rimay_results(response)




def setup_ui():

    make_intro_text()
    translation_buttons()

    #make_results()

