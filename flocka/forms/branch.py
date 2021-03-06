from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class BranchSlugField(StringField):

    def process_formdata(self, valuelist):
        if valuelist:
            if valuelist[0]:
                self.data = valuelist[0].strip()
            else:
                self.data = valuelist[0]


class BranchForm(Form):
    name = BranchSlugField(u'Name', validators=[DataRequired()])