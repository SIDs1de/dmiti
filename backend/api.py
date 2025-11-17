from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
from typing import Dict, List

# Добавляем путь для импорта ваших модулей
current_dir = os.path.dirname(__file__)
src_path = os.path.join(current_dir, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from src.integer import Integer
from src.natural import Natural
from src.rational import Rational
from src.polynomial import Polynomial

app = Flask(__name__)
CORS(app)


def dict_to_integer(data):
    """Преобразует словарь в объект Integer"""
    return Integer(data['sign'], Natural(list(map(int, list(str(data['absolute']))))))


def integer_to_dict(integer_obj):
    """Преобразует объект Integer в словарь"""
    return {
        "sign": integer_obj.sign,
        "absolute": integer_obj.absolute.digits,
        "string": str(integer_obj)
    }


def dict_to_natural(data: Dict[str, List[int]]) -> Natural:
    """Преобразует словарь в объект Natural"""
    return Natural(data['digits'])


def natural_to_dict(natural_obj):
    """Преобразует объект Natural в словарь"""
    return {
        "digits": natural_obj.digits,
        "string": str(natural_obj)
    }


def dict_to_rational(data):
    """Преобразует словарь в объект Rational"""
    numerator = dict_to_integer(data['numerator'])
    denominator = dict_to_natural(data['denominator'])
    return Rational(numerator, denominator)


def rational_to_dict(rational_obj):
    """Преобразует объект Rational в словарь"""
    return {
        "numerator": integer_to_dict(rational_obj.numerator),
        "denominator": natural_to_dict(rational_obj.denominator),
        "string": str(rational_obj)
    }


@app.route('/api/natural/com_nn_d', methods=['POST'])
def natural_com_nn_d():
    try:
        data = request.json
        a = dict_to_natural(data['a'])
        b = dict_to_natural(data['b'])
        result = a.COM_NN_D(b)
        return jsonify({
            "success": True,
            "result": result,
            "description": {
                0: "Числа равны",
                1: "Первое число меньше",
                2: "Первое число больше"
            }[result]
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/nzer_n_b', methods=['POST'])
def natural_nzer_n_b():
    try:
        data = request.json
        natural_obj = dict_to_natural(data)
        result = natural_obj.NZER_N_B()
        return jsonify({
            "success": True,
            "result": result.value,
            "description": {
                "да": "Это не ноль",
                "нет": "Это ноль"
            }[result.value]
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/add_1n_n', methods=['POST'])
def natural_add_one():
    try:
        data = request.json
        natural_obj = dict_to_natural(data)
        result = natural_obj.ADD_1N_N()
        return jsonify({
            "success": True,
            "result": natural_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/add_nn_n', methods=['POST'])
def natural_add():
    try:
        data = request.json
        a = dict_to_natural(data['a'])
        b = dict_to_natural(data['b'])
        result = a.ADD_NN_N(b)
        return jsonify({
            "success": True,
            "result": natural_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/sub_nn_n', methods=['POST'])
def natural_sub():
    try:
        data = request.json
        a = dict_to_natural(data['a'])
        b = dict_to_natural(data['b'])
        result = a.SUB_NN_N(b)
        return jsonify({
            "success": True,
            "result": natural_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/mul_nd_n', methods=['POST'])
def natural_mul_digit():
    try:
        data = request.json
        natural_obj = dict_to_natural(data['number'])
        digit = data['digit']
        result = natural_obj.MUL_ND_N(digit)
        return jsonify({
            "success": True,
            "result": natural_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/mul_nk_n', methods=['POST'])
def natural_mul_power():
    try:
        data = request.json
        natural_obj = dict_to_natural(data['number'])
        k = data['k']
        result = natural_obj.MUL_Nk_N(k)
        return jsonify({
            "success": True,
            "result": natural_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/mul_nn_n', methods=['POST'])
def natural_mul():
    try:
        data = request.json
        a = dict_to_natural(data['a'])
        b = dict_to_natural(data['b'])
        result = a.MUL_NN_N(b)
        return jsonify({
            "success": True,
            "result": natural_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/div_nn_dk', methods=['POST'])
def natural_div_digit():
    try:
        data = request.json
        a = dict_to_natural(data['a'])
        b = dict_to_natural(data['b'])
        k = data['k']
        result = a.DIV_NN_DK(b, k)
        return jsonify({
            "success": True,
            "result": result
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/div_nn_n', methods=['POST'])
def natural_div_nn_n():
    try:
        data = request.json
        a = dict_to_natural(data['a'])
        b = dict_to_natural(data['b'])
        result = a.DIV_NN_N(b)
        return jsonify({
            "success": True,
            "result": natural_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/mod_nn_n', methods=['POST'])
def natural_mod_nn_n():
    try:
        data = request.json
        a = dict_to_natural(data['a'])
        b = dict_to_natural(data['b'])
        result = a.MOD_NN_N(b)
        return jsonify({
            "success": True,
            "result": natural_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/sub_ndn_n', methods=['POST'])
def natural_sub_mul_digit():
    try:
        data = request.json
        a = dict_to_natural(data['a'])
        b = dict_to_natural(data['b'])
        digit = data['digit']
        result = a.SUB_NDN_N(b, digit)
        return jsonify({
            "success": True,
            "result": natural_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/gcf_nn_n', methods=['POST'])
def natural_gcf_nn_n():
    try:
        data = request.json
        a = dict_to_natural(data['a'])
        b = dict_to_natural(data['b'])
        result = a.GCF_NN_N(b)
        return jsonify({
            "success": True,
            "result": natural_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/lcm_nn_n', methods=['POST'])
def natural_lcm_nn_n():
    try:
        data = request.json
        a = dict_to_natural(data['a'])
        b = dict_to_natural(data['b'])
        result = a.LCM_NN_N(b)
        return jsonify({
            "success": True,
            "result": natural_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/integer/abs_z_n', methods=['POST'])
def integer_abs_z_n():
    try:
        data = request.json
        integer_obj = dict_to_integer(data)
        result_natural = integer_obj.abs_z_n()
        return jsonify({
            "success": True,
            "result": natural_to_dict(result_natural)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/integer/poz_z_d', methods=['POST'])
def integer_poz_z_d():
    try:
        data = request.json
        integer_obj = dict_to_integer(data)
        result_code = integer_obj.poz_z_d()
        return jsonify({
            "success": True,
            "result": result_code,
            "description": {
                0: "Ноль",
                1: "Отрицательное",
                2: "Положительное"
            }[result_code]
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/integer/mul_zm_z', methods=['POST'])
def integer_mul_zm_z():
    try:
        data = request.json
        integer_obj = dict_to_integer(data)
        result_integer = integer_obj.mul_zm_z()
        return jsonify({
            "success": True,
            "result": integer_to_dict(result_integer)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/natural/trans_n_z', methods=['POST'])
def natural_trans_n_z():
    try:
        data = request.json
        natural_obj = dict_to_natural(data)
        result = natural_obj.trans_n_z()
        return jsonify({
            "success": True,
            "result": integer_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/integer/trans_z_n', methods=['POST'])
def integer_trans_z_n():
    try:
        data = request.json
        integer_obj = dict_to_integer(data)
        result_natural = integer_obj.trans_z_n()
        return jsonify({
            "success": True,
            "result": natural_to_dict(result_natural)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/integer/add_zz_z', methods=['POST'])
def integer_add_zz_z():
    try:
        data = request.json
        a = dict_to_integer(data['a'])
        b = dict_to_integer(data['b'])
        result = a.add_zz_z(b)
        return jsonify({
            "success": True,
            "result": integer_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/integer/sub_zz_z', methods=['POST'])
def integer_sub_zz_z():
    try:
        data = request.json
        a = dict_to_integer(data['a'])
        b = dict_to_integer(data['b'])
        result = a.sub_zz_z(b)
        return jsonify({
            "success": True,
            "result": integer_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/integer/mul_zz_z', methods=['POST'])
def integer_mul_zz_z():
    try:
        data = request.json
        a = dict_to_integer(data['a'])
        b = dict_to_integer(data['b'])
        result = a.mul_zz_z(b)
        return jsonify({
            "success": True,
            "result": integer_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/integer/div_zz_z', methods=['POST'])
def integer_div_zz_z():
    try:
        data = request.json
        a = dict_to_integer(data['a'])
        b = dict_to_integer(data['b'])
        result = a.div_zz_z(b)
        return jsonify({
            "success": True,
            "result": integer_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/integer/mod_zz_z', methods=['POST'])
def integer_mod_zz_z():
    try:
        data = request.json
        a = dict_to_integer(data['a'])
        b = dict_to_integer(data['b'])
        result = a.MOD_ZZ_Z(b)
        return jsonify({
            "success": True,
            "result": integer_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/rational/add_qq_q', methods=['POST'])
def rational_add_qq_q():
    try:
        data = request.json
        a = dict_to_rational(data['a'])
        b = dict_to_rational(data['b'])
        result = a.ADD_QQ_Q(b)
        return jsonify({
            "success": True,
            "result": rational_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/rational/sub_qq_q', methods=['POST'])
def rational_sub_qq_q():
    try:
        data = request.json
        a = dict_to_rational(data['a'])
        b = dict_to_rational(data['b'])
        result = a.SUB_QQ_Q(b)
        return jsonify({
            "success": True,
            "result": rational_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/rational/mul_qq_q', methods=['POST'])
def rational_mul_qq_q():
    try:
        data = request.json
        a = dict_to_rational(data['a'])
        b = dict_to_rational(data['b'])
        result = a.MUL_QQ_Q(b)
        return jsonify({
            "success": True,
            "result": rational_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/rational/div_qq_q', methods=['POST'])
def rational_div_qq_q():
    try:
        data = request.json
        a = dict_to_rational(data['a'])
        b = dict_to_rational(data['b'])
        result = a.DIV_QQ_Q(b)
        return jsonify({
            "success": True,
            "result": rational_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/rational/int_q_b', methods=['POST'])
def rational_int_q_b():
    try:
        data = request.json
        rational_obj = dict_to_rational(data)
        result = rational_obj.INT_Q_B()
        return jsonify({
            "success": True,
            "result": result,
            "description": {
                "да": "Дробь является целым числом",
                "нет": "Дробь не является целым числом"
            }[result]
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/rational/red_q_q', methods=['POST'])
def rational_red_q_q():
    try:
        data = request.json
        rational_obj = dict_to_rational(data)
        result = rational_obj.RED_Q_Q()
        return jsonify({
            "success": True,
            "result": rational_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/rational/trans_z_q', methods=['POST'])
def rational_trans_z_q():
    try:
        data = request.json
        integer_obj = dict_to_integer(data)
        result = Rational(integer_obj, Natural([1])).TRANS_Z_Q(integer_obj)
        return jsonify({
            "success": True,
            "result": rational_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/rational/trans_q_z', methods=['POST'])
def rational_trans_q_z():
    try:
        data = request.json
        rational_obj = dict_to_rational(data)
        result = rational_obj.TRANS_Q_Z()
        return jsonify({
            "success": True,
            "result": integer_to_dict(result)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "success": True,
        "result": "Algebra system API is running"
    })


if __name__ == '__main__':
    print("✅ Starting API server on http://localhost:5010")
    app.run(host='0.0.0.0', port=5010, debug=True)
