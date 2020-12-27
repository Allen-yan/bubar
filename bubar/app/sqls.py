

max_factor = """
    SELECT max(pipe_id_max) FROM app_factor WHERE flow_type ="{}" 
"""


min_factor = """
    SELECT min(pipe_id_min) FROM app_factor WHERE flow_type ="{}" 
"""

