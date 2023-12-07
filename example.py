from algorithm import find_path
from tests import HiddenPrints

# Problem: Use the cheapest insertion algorithm to find a hamiltonian cycle in the graph
def tsp_cheapest_insertion_example():
    with HiddenPrints('example'):
        path, price, subs = find_path('example.txt')
    
    expected_path = [1,2,4,5,3]
    expected_price = 19
    expected_sub_paths = [[1], [1,5], [1,4,5], [1,2,4,5], [1,2,4,5,3]]
    
    print('Expected path: ', expected_path)
    print('Actual path: ', path)
    print('Expected price: ', expected_price)
    print('Actual price: ', price)
    print('Expected sub paths: ', expected_sub_paths)
    print('Actual sub paths: ', subs)
    
if __name__ == '__main__':
    tsp_cheapest_insertion_example()