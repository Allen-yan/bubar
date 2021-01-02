import logging

from django import forms

logger = logging.getLogger("app")

class AccountActionForm(forms.Form):
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea,
    )
    send_email = forms.BooleanField(
        required=False,
    )

    @property
    def email_subject_template(self):
        return 'email/account/notification_subject.txt'


def _clean_form(form_validator, payload):
    result = {}
    for f, (f_type, f_required) in form_validator.items():
        logger.debug("validate field {}, {}, {}".format(f, f_type, f_required))
        if f in payload:
            try:
                result[f] = f_type(payload[f])
            except ValueError:
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
