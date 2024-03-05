import asyncio
from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from nicegui import run, ui
from random import random
from contextlib import contextmanager

from wrapper_calls import ask_different_prompts


#['Few-shot learning', 'Chain-of-thought', 'Role play']
translation_type = "Few-shot learning" #fsl, cot, rp
input_text = ""
current_result = 0

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

def make_intro_text():
    global input_text
    ui.markdown('# Translate Gherkin to Rimay')
    ui.markdown("Uses different prompting techniques to translate Gherkin (Given When Then) into Rimay (CNL)")
    ui.markdown("The following prompt techniques will be used:")
    ui.markdown("* Few-shot learning")
    ui.markdown("* Chain-of-thought")
    ui.markdown("* Role-play")
    with ui.card():
        with ui.card_section():
            ui.markdown("## Input Gherkin")

            ui.textarea(label='Acceptance Criteria', placeholder='start typing',
                        on_change=lambda e: set_input_text(e.value))
            result = ui.label()

def translation_buttons():
     with ui.card():
        with ui.card_section():

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
            ui.label('This is some content on the left hand side.').classes('mr-40')
        with splitter.after:
            ui.markdown("#### Rimay").classes('ml-40')
            ui.label('This is some content on the right hand side.').classes('ml-40')


def paska_tooling_result():
    ui.markdown("#### Paska tooling output")
    ui.label('Test for paska tooing output.').classes('mr-40')


def make_results(result):
    ui.markdown("### Result translation " + str(current_result))
    ui.markdown("Result was: " + result)

    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'left'},
        {'name': 'link', 'label': 'Link', 'field': 'link', 'align': 'left'},
    ]
    rows = [
        {'name': 'Google', 'link': 'https://google.com'},
        {'name': 'Facebook', 'link': 'https://facebook.com'},
        {'name': 'Twitter', 'link': 'https://twitter.com'},
    ]
    table = ui.table(columns=columns, rows=rows, row_key='name')
    table.add_slot('body-cell-link', '''
        <q-td :props="props">
            <a :href="props.value">{{ props.value }}</a>
        </q-td>
    ''')


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


def show_all_results(response):
    make_results(response)
    paska_tooling_result()
    compare_translations()
    ui.html("<br>")

    ui.separator().props('inline color=red')



async def start_translation(button: ui.button):
    global current_result
    button.disable()
    ui.html("<br>")
    current_result += 1
    spinner = ui.spinner(size='lg', color='blue')

    response = await run.io_bound(ask_different_prompts, input_text, translation_type)
    button.enable()
    spinner.delete()
    show_all_results(response)



def setup_ui():

    make_intro_text()
    translation_buttons()


    #make_results()

