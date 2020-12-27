import logging
from django.db import connections

logger = logging.getLogger('app')


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def db_fetch_one(sql, db='default'):
    logger.debug(sql)
    with connections[db].cursor() as cursor:
        cursor.execute(sql)

        result = cursor.fetchone()

    return result[0] if result else None


def db_execute(sql, db='default'):
    logger.debug(sql)
    with connections[db].cursor() as cursor:
        result = cursor.execute(sql)

    return result


def gen_in_sql(str_list):
    return "'" + "','".join(str_list) + "'"


def db_fetch(sql, db='default', result_type='d'):
    """

    :param sql:
    :param db:
    :param result_type:  默认d 返回字典， l 为list
    :return:
    """
    logger.debug(sql)
    with connections[db].cursor() as cursor:
        cursor.execute(sql)

        if result_type == 'l':
            result = cursor.fetchall()
        else:
            result = dictfetchall(cursor)

    return result
