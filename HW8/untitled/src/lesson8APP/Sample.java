package lesson8APP;

import lesson8APP.models.Tablemodel;
import lesson8APP.presenters.BookingPresenter;
import lesson8APP.views.BookingView;

import java.util.Date;

public class Sample {
    public static void main(String[] args) {
        Tablemodel tablemodel = new Tablemodel();
        BookingView view = new BookingView();
        BookingPresenter presenter = new BookingPresenter(tablemodel, view);

        presenter.loadTables();
        presenter.updateView();

        view.reservationTable(new Date(),3,"Севик");

    }
}