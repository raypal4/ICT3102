from flask import Blueprint

# Initialization
router = Blueprint("tempRoute", __name__)

@router.route("/test-route", methods=['GET', 'POST'])
def test():
    return f"return API Call here"