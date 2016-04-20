package controllers;

import play.*;
import play.mvc.*;
import play.db.jpa.*;
import views.html.*;
import models.Value;
import play.data.Form;
import play.data.FormFactory;
import javax.inject.Inject;
import java.util.List;

import static play.libs.Json.*;

public class Test2 extends Controller {

    private int iVal = 0;

    @Inject
    FormFactory formFactory;

    @Transactional
    public Result valueSub() {
        Form<Value> valueForm = formFactory.form(Value.class);
        Value value = valueForm.bindFromRequest().get();
        JPA.em().persist(value);
        if (value.getData().equals("x"))
        {
            iVal -= 1;
        }
        return redirect(routes.Application.index());
    }

    @Transactional
    public Result valueAdd() {
        Form<Value> valueForm = formFactory.form(Value.class);
        Value value = valueForm.bindFromRequest().get();
        JPA.em().persist(value);
        if (value.getData().equals("x"))
        {
            iVal += 1;
        }
        return redirect(routes.Application.index());
    }

    @Transactional(readOnly = true)
    public Result getValues() {
        List<Value> values = (List<Value>) JPA.em().createQuery("select v from Value v").getSingleResult();
        return ok(toJson(values));
    }

    @Transactional(readOnly = true)
    public Result getDisplay() {
        return ok("" + iVal);
    }
}
