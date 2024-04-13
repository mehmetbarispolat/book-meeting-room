import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import "react-datepicker/dist/react-datepicker.css";

function BookingForm({ onSearch }) {
    const [attendees, setAttendees] = useState(1);
    const [startDate, setStartDate] = useState(new Date());
    const [endDate, setEndDate] = useState(new Date());

    const handleSubmit = (event) => {
        event.preventDefault();
        onSearch(attendees, { startDate, endDate });
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Number of Attendees:
                <input
                    type="number"
                    value={attendees}
                    onChange={(e) => setAttendees(parseInt(e.target.value, 10))}
                    min="1"
                />
            </label>
            <label>
                Start Date:
                <DatePicker
                    selected={startDate}
                    onChange={date => setStartDate(date)}
                    selectsStart
                    startDate={startDate}
                    endDate={endDate}
                />
            </label>
            <label>
                End Date:
                <DatePicker
                    selected={endDate}
                    onChange={date => setEndDate(date)}
                    selectsEnd
                    startDate={startDate}
                    endDate={endDate}
                    minDate={startDate}
                />
            </label>
            <button type="submit">Search Rooms</button>
        </form>
    );
}

export default BookingForm;
