import pytest
import tkinter as tk
from project import setdisp, setoperator, ans, cl

@pytest.fixture
def mock_entry():
    root = tk.Tk()
    entry = tk.Entry(root)
    yield entry
    root.destroy()

@pytest.fixture
def mock_state():
    return []

def test_setdisp(mock_entry):
    result = setdisp(mock_entry, 2)
    assert result == 2
    assert mock_entry.get() == "2"

def test_setoperator(mock_state, mock_entry):
    mock_entry.insert(0, "5")
    operator = "+"
    result = setoperator(mock_state, mock_entry, operator)
    assert result == operator
    assert mock_state == ["5", "+"]
    assert mock_entry.get() == ""

def test_ans(mock_state, mock_entry):
    mock_state.extend(["5", "+"])
    mock_entry.insert(0, "3")
    ans(mock_state, mock_entry)
    assert mock_entry.get() == "8"
    mock_entry.insert(0,"*")
    mock_entry.insert(0,"8")
    ans(mock_state, mock_entry)
    assert mock_entry.get() == "64"

def test_cl(mock_entry):
    mock_entry.insert(0, "35")
    cl(mock_entry)
    assert mock_entry.get() == ""
