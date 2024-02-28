import asyncio
from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from nicegui import run, ui
from random import random
from contextlib import contextmanager

from wrapper_calls import ask_different_prompts


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


def make_intro_text():
    ui.markdown('# Translate Gherkin to Rimay')
    ui.markdown("Uses different prompting techniques to translate Gherkin (Given When Then) into Rimay (CNL)")

    ui.markdown("## Input text")

    ui.textarea(label='Text', placeholder='start typing',
                on_change=lambda e: result.set_text('you typed: ' + e.value))
    result = ui.label()


def translation_buttons():
     with ui.card():
        with ui.card_section():

            ui.markdown("### Translation technique")
            with ui.row():
                ui.radio(['Few-shot learning', 'Chain-of-thought', 'Role play'], value='Few-shot learning', on_change=show).props('inline')
            ui.separator()
            ui.button('Translate', on_click=lambda e: start_translation(e.sender))


def compare_translations():
    ui.markdown("### Translation result")
    with ui.splitter() as splitter:

        with splitter.before:
            ui.markdown("#### Gherkin").classes('mr-40')
            ui.label('This is some content on the left hand side.').classes('mr-40')
        with splitter.after:
            ui.markdown("#### Rimay").classes('ml-40')
            ui.label('This is some content on the right hand side.').classes('ml-40')


def paska_tooling_result():
    ui.markdown("### Paska tooling output")
    ui.label('Test for paska tooing output.').classes('mr-40')


def make_results(result):
    ui.markdown("### Result translation")
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



def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')


@contextmanager
def disable(button: ui.button):
    button.disable()
    try:
        yield
    finally:
        button.enable()

async def start_translation(button: ui.button):
    URL = 'https://httpbin.org/delay/1'
    response = await run.io_bound(ask_different_prompts)
    ui.notify(f'Downloaded {response} bytes')

# def start_translation(event: ValueChangeEventArguments):
#     name = type(event.sender).__name__
#     background_worker(make_results)

#     ui.notify(f'Starting translation wait...')


def setup_ui():

    make_intro_text()
    translation_buttons()
    compare_translations()

    paska_tooling_result() 

    #make_results()

