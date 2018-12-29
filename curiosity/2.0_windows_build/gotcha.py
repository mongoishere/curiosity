# List representing Transition Matrix 
import random
from difflib import SequenceMatcher
import operator
import functools
import pprint
import collections

# XXX: ONLY WORKS WITH 1-STATE LH MARKOV MODELS, NOT 2-STATE LH!

RUN_TIMES = 100000

HISTORY = ['R', 'D']
TRANSITION_MATRIX = [[0.25, 0.75], [0.5, 0.5]]
STATES = ['D', 'R']

starting_state_index = STATES.index(HISTORY[0])
state_results = []
history_length = len(HISTORY)
history_as_string = functools.reduce(operator.concat, HISTORY)
pp = pprint.PrettyPrinter(indent=4)

for x in range(RUN_TIMES):
    current_state = starting_state_index
    current_state_history = [current_state]

    for y in range(history_length - 1):
        random_number = random.uniform(0, 1.01)

        if random_number > 1:
            random_number = 1

        previous_boundary = 0.0
        choice_index = 0

        for prob in TRANSITION_MATRIX[current_state]:
            if previous_boundary + prob >= random_number:
                current_state = choice_index
                current_state_history.append(choice_index)
                break
            else:
                previous_boundary += prob
                choice_index += 1

    state_results.append(current_state_history)

end_stats = {}
for state_result_history_index in range(len(state_results)):
    state_result_history = state_results[state_result_history_index]

    history_string = ""
    for state_index in state_result_history:
        history_string += STATES[state_index]

    if history_string in end_stats:
        end_stats[history_string]['count'] = end_stats[history_string]['count'] + 1
    else:
        assert len(history_string) == len(history_as_string)
        likeness = SequenceMatcher(None, history_string, history_as_string).ratio()
        end_stats[history_string] = { 'likeness': likeness, 'count': 1 }

#pp.pprint(end_stats)

end_output = collections.OrderedDict(sorted(end_stats.items(), key=lambda item: item[1]['likeness'], reverse=True))

for history, stats in end_output.items():
    print('"{}" ({:.2f}% similar to history): occurred {:.2f}% of the time ({} times)'.format(history, stats['likeness']*100, stats['count']/RUN_TIMES*100, stats['count']))
