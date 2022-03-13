from SALib.sample import fast_sampler

from Discretizers.discretizer_base import Basediscretizer
import numpy as np
import copy

class FastDiscretizer(Basediscretizer):

    @classmethod
    def _discrete(cls, params):
        problem = create_discrete_problem(params)
        param_values = create_param_values(problem)
        params_list = []
        for params in param_values:
            discreted_params = {xpath: param for xpath, param in zip(problem['names'], params)}
            params_list.append(discreted_params)
        return params_list


def create_discrete_problem(params):
    problem = {
        'num_vars': 0,
        'names': [],
        'bounds': []
    }
    for xpath, value in params.items():
        problem['num_vars'] += 1
        problem['names'].append(xpath)
        problem['bounds'].append([value[0], value[1], int(value[2])])
    return problem

def create_param_values(problem):
    param_values = []
    for i, bound in enumerate(problem['bounds']):
        aa = np.linspace(bound[0],bound[1],bound[2])
        if i == 0:
            for item1 in aa:
                param_values.append([item1])

        if i > 0:
            param_values_sum = copy.deepcopy(param_values)
            for item2 in param_values_sum:
                param_values.remove(item2)
                for item1 in aa:
                    cc = item2 + [item1]
                    param_values.append(cc)
    return param_values