package models;

import javax.persistence.*;

@Entity
public class Thing {

    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    public String id;

    public String thingName;

    public String toString()
    {
        return this.thingName + ", " + this.id;
    }
}
