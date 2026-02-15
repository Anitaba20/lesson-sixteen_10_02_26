class Form:
    def __init__(self):
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)

    def __str__(self):
        return "\n".join(self.fields)


class FormBuilder:
    def __init__(self):
        self.form = Form()

    def add_name_field(self):
        self.form.add_field("Name: [__________]")
        return self

    def add_address_field(self):
        self.form.add_field("Address: [__________]")
        return self

    def add_email_field(self):
        self.form.add_field("Email: [__________]")
        return self

    def build(self):
        return self.form


builder = FormBuilder()
form = builder.add_name_field().add_address_field().add_email_field().build()
print(form)
