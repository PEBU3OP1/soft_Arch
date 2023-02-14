package lesson8APP.presenters;

import lesson8APP.models.Table;

import java.util.Collection;

public interface View {

    void showTables(Collection<Table> tables);
    void setObserver(ViewObserver observer);
    void printReservayionTableResult(int reservationNo);
    void changeReservationTableResult(int newReservationNo);
}
