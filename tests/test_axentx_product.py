import pytest
from src.axentx_product import chain
from src.axentx_product import brain
from src.axentx_product import step

def test_brain():
    brain_instance = brain.Brain()
    brain_instance.add_knowledge("key", "value")
    assert brain_instance.knowledge["key"] == "value"

def test_chain():
    chain_instance = chain.Chain()
    step_instance = step.Step("test_step")
    chain_instance.add_step(step_instance)
    chain_instance.run()

def test_step():
    step_instance = step.Step("test_step")
    brain_instance = brain.Brain()
    step_instance(brain_instance)
