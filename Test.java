package controllers;

import play.*;
import play.mvc.*;
import play.db.jpa.*;
import views.html.*;
import models.Thing;
import play.data.Form;
import play.data.FormFactory;
import javax.inject.Inject;
import java.util.List;

import static play.libs.Json.*;

public class Test extends Controller {

    @Inject
    FormFactory formFactory;

    @Transactional
    public Result addThing() {
        Form<Thing> thingForm = formFactory.form(Thing.class);
        Thing thing = thingForm.bindFromRequest().get();
        JPA.em().persist(thing);
        return redirect(routes.Application.index());
        //return ok(thing.toString());
    }

    @Transactional(readOnly = true)
    public Result getThings() {
        List<Thing> things = (List<Thing>) JPA.em().createQuery("select t from Thing t").getResultList();
        return ok(toJson(things));
    }
}
