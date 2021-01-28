import logging
import json
import traceback

from django.utils import timezone
from django import forms

logger = logging.getLogger("app")


def serializer_history_operation(obj):
    result = {}
    for i in vars(obj):
        if i in ['data', 'result']:
            tmp = json.loads(getattr(obj, i))
            result.update(tmp)
        elif i in ('_state', ):
            continue
        elif i == "create_time":
            result['create_time'] = timezone.localtime(obj.create_time).strftime("%Y-%m-%d %H:%M")
        elif i == 'flow_factor':
            result['flow_factor'] = float(getattr(obj, i))
        else:
            result[i] = getattr(obj, i)

    return result


def _clean_form(form_validator, payload):
    result = {}
    for f, (f_type, f_required) in form_validator.items():
        logger.debug("validate field {}, {}, {}".format(f, f_type, f_required))
        if f in payload:
            try:
                if payload[f]:
                    result[f] = f_type(payload[f])
                elif f_required:
                    return False, "{} require {}!".format(f, str(f_type))
            except ValueError:
                logger.warning("{} error\n{}".format(f, traceback.format_exc(1)))
                return False, "{} require {}!".format(f, str(f_type))
        else:
            if f_required:
                return False, "{} required".format(f)

    return True, result


def gas_dp_form_clean(payload):
    form_validator = {  # key: (type, required)
        'pipe_id': (float, True),
        'pf': (float, True),
        'tf': (float, True),
        'flow_rate_min': (float, False),
        'flow_rate_nor': (float, False),
        'flow_rate_max': (float, False),
        'flow_rate_c': (float, True),
        'mw': (float, True),
        'tb': (float, True),
        'pb': (float, True),

        'project_name': (str, True),
        'operator': (str, True),
        'page': (str, True),
        'fluid': (str, True),
        'tag_number': (str, True),
        'pipe_od': (str, True),
        'pipe_material': (str, True),
        'pipe_direction': (str, True),
        'press_rating': (str, True),
        'pipe_orientation': (str, True),
        'dp_conn_type': (str, True),
    }

    return _clean_form(form_validator, payload)


def gas_qv_form_clean(payload):
    form_validator = {  # key: (type, required)
        'pipe_id': (float, True),
        'pf': (float, True),
        'tf': (float, True),
        'flow_rate_min': (float, False),
        'flow_rate_nor': (float, False),
        'flow_rate_max': (float, False),
        'flow_rate_c': (float, True),
        'mw': (float, True),
        'tb': (float, True),
        'pb': (float, True),
        'dp': (float, True),

        'project_name': (str, True),
        'operator': (str, True),
        'page': (str, True),
        'fluid': (str, True),
        'tag_number': (str, True),
        'pipe_od': (str, True),
        'pipe_material': (str, True),
        'pipe_direction': (str, True),
        'press_rating': (str, True),
        'pipe_orientation': (str, True),
        'dp_conn_type': (str, True),
    }

    return _clean_form(form_validator, payload)


def liquid_dp_form_clean(payload):
    form_validator = {  # key: (type, required)
        'pipe_id': (float, True),
        'pf': (float, False),
        'tf': (float, False),
        'flow_rate_min': (float, False),
        'flow_rate_nor': (float, False),
        'flow_rate_max': (float, False),
        'flow_rate_c': (float, True),
        'gf': (float, True),
        'tb': (float, False),
        'pb': (float, False),

        'project_name': (str, True),
        'operator': (str, True),
        'page': (str, True),
        'fluid': (str, True),
        'tag_number': (str, True),
        'pipe_od': (str, True),
        'pipe_material': (str, True),
        'pipe_direction': (str, True),
        'press_rating': (str, True),
        'pipe_orientation': (str, True),
        'dp_conn_type': (str, True),
    }

    return _clean_form(form_validator, payload)


def steam_dp_form_clean(payload):
    form_validator = {  # key: (type, required)
        'pipe_id': (float, True),
        'pf': (float, False),
        'tf': (float, False),
        'flow_rate_min': (float, False),
        'flow_rate_nor': (float, False),
        'flow_rate_max': (float, False),
        'flow_rate_c': (float, True),
        'od': (float, True),
        'tb': (float, False),
        'pb': (float, False),

        'project_name': (str, True),
        'operator': (str, True),
        'page': (str, True),
        'fluid': (str, True),
        'tag_number': (str, True),
        'pipe_od': (str, True),
        'pipe_material': (str, True),
        'pipe_direction': (str, True),
        'press_rating': (str, True),
        'pipe_orientation': (str, True),
        'dp_conn_type': (str, True),
    }

    return _clean_form(form_validator, payload)



def liquid_qm_form_clean(payload):
    form_validator = {  # key: (type, required)
        'pipe_id': (float, True),
        'pf': (float, False),
        'tf': (float, False),
        'flow_rate_min': (float, False),
        'flow_rate_nor': (float, False),
        'flow_rate_max': (float, False),
        'dp': (float, True),
        'gf': (float, True),
        'tb': (float, False),
        'pb': (float, False),

        'project_name': (str, True),
        'operator': (str, True),
        'page': (str, True),
        'fluid': (str, True),
        'tag_number': (str, True),
        'pipe_od': (str, True),
        'pipe_material': (str, True),
        'pipe_direction': (str, True),
        'press_rating': (str, True),
        'pipe_orientation': (str, True),
        'dp_conn_type': (str, True),
    }

    return _clean_form(form_validator, payload)
