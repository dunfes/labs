if content_type == 'application/json':
        # JSON
        response = {
            "status": "success",
            "message": "JSON response",
            "data": {
                "currency": "USD",
                "rate": "41.5"
            }
        }
        return jsonify(response)
    
    elif content_type == 'application/xml':
        # XML
        xml_response = '''<?xml version="1.0" encoding="UTF-8"?>
<data>
    <status>success</status>
    <message>XML response</message>
    <currency>USD</currency>
    <rate>41.5</rate>
</data>'''
        return Response(xml_response, mimetype='application/xml')
    
    else:
        return "just texts."

if __name__ == '__main__':
    app.run(port=8000, debug=True)
