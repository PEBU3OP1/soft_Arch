package lesson8APP.presenters;

import java.util.Date;

public interface ViewObserver {
    void onReservationTable(Date orderDate, int tableNo, String name);
}
