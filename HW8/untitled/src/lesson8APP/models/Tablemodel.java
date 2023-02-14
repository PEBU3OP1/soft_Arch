package lesson8APP.models;

import lesson8APP.presenters.Model;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Date;
import java.util.Optional;

public class Tablemodel implements Model {

    private Collection<Table> tables;
    public Collection<Table> loadTables(){
        if (tables == null)
            tables = new ArrayList<>();

        tables.add(new Table());
        tables.add(new Table());
        tables.add(new Table());
        tables.add(new Table());
        tables.add(new Table());

        return tables;

    }

    /**
     *
     * @param reservationDate дата бронировния
     * @param tableNo номер стола
     * @param name имя клиента
     * @return номер брони
     */
    public int reservationTable (Date reservationDate, int tableNo, String name){
        Optional<Table> table = loadTables().stream().filter(t -> t.getNo() == tableNo).findFirst();
        if (table.isPresent()){
            //TODO: проверка резерва
            Reservation reservation = new Reservation(reservationDate, name);
            table.get().getReservations().add(reservation);
            return reservation.getId();
        }
        throw new RuntimeException("Номер стола некорректен");
    }

    public int changeReservationTable(int oldReservation, Date orderDate, int tableNo, String name){
        Optional<Table> table = loadTables().stream().filter(t -> t.getNo() == tableNo).findFirst();
        if(table.isPresent()){
            table.get().getReservations().clear();
            int newReservationId = reservationTable(orderDate,tableNo,name);
            return newReservationId;

        }
        throw new RuntimeException("Номер стола некорректен");
    }
}
