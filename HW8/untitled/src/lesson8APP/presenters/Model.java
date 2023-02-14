package lesson8APP.presenters;

import lesson8APP.models.Table;

import java.util.Collection;
import java.util.Date;

public interface Model {
    Collection<Table> loadTables();
    int reservationTable (Date reservationDate, int tableNo, String name);
}
