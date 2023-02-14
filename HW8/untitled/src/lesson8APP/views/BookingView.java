package lesson8APP.views;

import com.sun.jdi.Value;
import lesson8APP.models.Table;
import lesson8APP.presenters.View;
import lesson8APP.presenters.ViewObserver;

import java.util.Collection;
import java.util.Date;

public class BookingView implements View {
    private ViewObserver observer;

    public void setObserver(ViewObserver observer) {
        this.observer = observer;
    }

    public void showTables(Collection<Table> tables) {
        for (Table table : tables) {
            System.out.println(table);

        }
    }

    public void reservationTable(Date orderDate, int tableNo, String name) {
        observer.onReservationTable(orderDate, tableNo, name);

    }

    public void changeReservationTable(int oldReservation, Date orderDate, int tableNo, String name){
        observer.onChangeReservationTable(oldReservation,orderDate,tableNo,name);
    }

    public void printReservayionTableResult(int reservationNo){
        System.out.printf("Стол успешно забронирован. Номер брони: %d\n",reservationNo);
    }

    public void changeReservationTableResult(int newReservationNo){
        System.out.println("Бронь отменена!");
        System.out.printf("Новый стол успешно забронирован. Номер новой брони: %d\n", newReservationNo);
    }
}
