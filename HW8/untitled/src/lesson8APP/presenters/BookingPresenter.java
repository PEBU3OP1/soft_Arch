package lesson8APP.presenters;

import lesson8APP.models.Table;

import javax.management.modelmbean.ModelMBean;
import java.util.Collection;
import java.util.Date;
import java.util.Optional;

public class BookingPresenter implements ViewObserver{

    private final Model model;
    private View bookingView;
    private Collection<Table> tables;

    public BookingPresenter(Model model, View view){
        this.model = model;
        this.bookingView = view;
        view.setObserver(this);
    }

    /**
     * ПОлучение списка всех столов
     */
    public void loadTables(){
        tables = model.loadTables();
    }

    /**
     * Отобразить список всех столов на представлении
     */
    public void updateView(){
    bookingView.showTables(tables);

    }

    public void printReservayionTableResult(int reservationNo){
        bookingView.printReservayionTableResult(reservationNo);
    }

    public void changeReservationTableResult(int newReservationNo){
        bookingView.changeReservationTableResult(newReservationNo);
    }
    /***
     * Произошло событие, клиент нажал на кнопку резрва стола
     * @param orderDate
     * @param tableNo
     * @param name
     */
    public void onReservationTable(Date orderDate, int tableNo, String name){
        Optional<Table> table = tables.stream().filter(t -> t.getNo() == tableNo).findFirst();
        if (table.isPresent()) {
            int reservationNo = model.reservationTable(orderDate, tableNo, name);
            //BookingPresenter сообщает представлению View об успешном бронировании
            printReservayionTableResult(reservationNo);
        }
    }
    public void onChangeReservationTable(int oldReservation, Date orderDate, int tableNo, String name){
        Optional<Table> table = tables.stream().filter(t -> t.getNo() == tableNo).findFirst();
        if(table.isPresent()){
            int newReservationNo = model.changeReservationTable(oldReservation,orderDate,tableNo,name);
            changeReservationTableResult(newReservationNo);
        }
    }
}
