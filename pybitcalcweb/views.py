from flask import render_template, redirect, url_for, request, flash
from pybitcalcweb import app
from collections import OrderedDict
from . import bitcalc


@app.route('/')
def site_root():
    """ Default site route, redirects to calulator """
    return redirect(url_for('calculator'))


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """ Catch all path, credit to Oli -http://flask.pocoo.org/snippets/57/ """
    return redirect(url_for('calculator'))


@app.route('/calculator')
def calculator():
    """ Bit calculator view input and output handling (needs refactoring) """

    # Valid input definitions, used in form field building and input validation
    input_map = OrderedDict()
    input_map['prefix'] = OrderedDict()
    input_map['type'] = OrderedDict()
    input_map['base'] = OrderedDict()
    input_map['prefix']['none'] = '-'
    input_map['prefix']['kilo'] = 'Kilo (K)'
    input_map['prefix']['mega'] = 'Mega (M)'
    input_map['prefix']['giga'] = 'Giga (G)'
    input_map['prefix']['tera'] = 'Tera (T)'
    input_map['prefix']['peta'] = 'Peta (P)'
    input_map['type']['bit'] = 'bit (b)'
    input_map['type']['byte'] = 'byte (B)'
    input_map['base']['base-2'] = 'base-2 (1024)'
    input_map['base']['base-10'] = 'base-10 (1000)'

    # Valid argument definitions
    valid_arguments = ('amount', 'prefix', 'type', 'base')
    valid_arg_count = 0
    required_arg_count = len(valid_arguments)

    # Check arguments against valid_arguments tuple and log any errors
    argument_errors = []

    # Return error if more args than required are passed
    arg_count = len(request.args)

    if arg_count > 4:
        error = "Too many arguments: {}".format(arg_count)
        flash(error)
        return redirect(url_for('calculator'))

    # Format and define errors for any invalid args
    for key in request.args:
        if key not in valid_arguments:
            error = "'{}' is not a valid argument: {}".format(
                key,
                valid_arguments)
            argument_errors.append(error)

    # Flash invalid arg errors
    if len(argument_errors) > 0:
        for error in argument_errors:
            flash(error)
        return redirect(url_for('calculator'))

    # Build user_input dict
    user_input = {}
    for argument in valid_arguments:
        user_input[argument] = request.args.get(argument)

    # Check if arguments are valid
    for key in user_input:
        # Increment valid_arg_count if the user provided any input (not None)
        valid_arg_count += 1 if user_input[key] is not None else 0

    # Fail argument list if any argument is not valid
    required_args = False if valid_arg_count < required_arg_count else True

    if not required_args:
        # Return basic template with input_map to populate form fields
        return render_template(
            'calculator.html',
            input_map=input_map)
    else:
        # Run through logic to build and ship conversion table values
        validated_input = bitcalc.validate_input(user_input, input_map)

        if len(validated_input['errors']) > 0:
            for error in validated_input['errors']:
                flash(error)
            return redirect(url_for('calculator'))

        bit_value = bitcalc.convert_amount_to_bits(
            validated_input['amount'],
            validated_input['prefix'],
            validated_input['type'],
            validated_input['base'])

        conversion_table = bitcalc.generate_conversion_table(
            bit_value,
            validated_input['base'])

        return render_template(
            'calculator.html',
            input_map=input_map,
            validated_input=validated_input,
            conversion_table=conversion_table)
