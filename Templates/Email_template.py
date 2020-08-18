email_template_html = """\
<html>
    <body>
    {% for key, value in stocks.items() %}
        <h3>{{key}}</h3>
        <p>Current price: {{value['sell_price']}}€</p>
        <p>Target sell price: {{value['target_price']}}€</p>
        <p>Increase at least {{value['increase']}}% from purchase price</p>
    {% endfor %}
    </body>
</html>
"""