from IPython.display import Image, display
import operator
from typing import Annotated, List, Literal, TypedDict
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


#state
class State(TypedDict):
    nlist : Annotated[List[str],operator.add]

#nodes
def node_a(state: State) -> State:
    print(f"Adding 'A' to {state['nlist']}")
    return State(nlist = ["A"])

def node_b(state: State) -> State:
    print(f"Adding 'B' to {state['nlist']}")
    return State(nlist = ["B"])

def node_c(state: State) -> State:
    print(f"Adding 'C' to {state['nlist']}")
    return State(nlist = ["C"])

def node_d(state: State) -> State:
    print(f"Adding 'D' to {state['nlist']}")
    return State(nlist = ["D"])

def node_bb(state: State) -> State:
    print(f"Adding 'BB' to {state['nlist']}")
    return State(nlist = ["BB"])

def node_cc(state: State) -> State:
    print(f"Adding 'CC' to {state['nlist']}")
    return State(nlist = ["CC"])

def node_dd(state: State) -> State:
    print(f"Adding 'DD' to {state['nlist']}")
    return State(nlist = ["DD"])

def node_e(state: State) -> State:
    print(f"Adding 'E' to {state['nlist']}")
    return State(nlist = ["E"])


if __name__ == '__main__':
    builder = StateGraph(State)

    #Add nodes
    builder.add_node("a",node_a)
    builder.add_node("b",  node_b)
    builder.add_node("c", node_c)
    builder.add_node("d", node_d)
    builder.add_node("bb", node_bb)
    builder.add_node("cc", node_cc)
    builder.add_node("dd", node_dd)
    builder.add_node("e", node_e)

    #Add edges
    builder.add_edge(START,"a")
    builder.add_edge("a","b")
    builder.add_edge("a","c")
    builder.add_edge("a","d")
    builder.add_edge("b","bb")
    builder.add_edge("c","cc")
    builder.add_edge("d","dd")
    builder.add_edge("bb","e")
    builder.add_edge("cc","e")
    builder.add_edge("dd","e")
    builder.add_edge("e",END)

    graph = builder.compile()
    print(graph.get_graph().draw_mermaid())

    initial_state = State(
        nlist=["Initial State"],
    )

    result = graph.invoke(initial_state)

    print(f"Final nlist: {result['nlist']}")

