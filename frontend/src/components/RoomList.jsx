import { useEffect, useState } from 'react';
import axios from 'axios';

function RoomList({ attendees, timeframe }) {
    const [rooms, setRooms] = useState([]);

    useEffect(() => {
        if (attendees && timeframe) {
            let params = {
                number_of_people: attendees,
                start_time: timeframe.startDate,
                end_time: timeframe.endDate
            }
            axios.get(`http://localhost:8000/api/availablerooms`, {
                params
            })
            .then(response => setRooms(response.data))
            .catch(error => console.error('Error fetching rooms:', error));
        }
    }, [attendees, timeframe]);

    const bookRoom = (roomId) => {
        axios.post(`http://localhost:8000/api/bookroom`, {
            roomId,
            timeframe
        })
        .then(() => alert('Room booked successfully!'))
        .catch(error => console.error('Error booking room:', error));
    };

    return (
        <ul>
            {rooms.map(room => (
                <li key={room.id}>
                    {room.name} - Capacity: {room.capacity}
                    <button onClick={() => bookRoom(room.id)}>Book</button>
                </li>
            ))}
        </ul>
    );
}

export default RoomList;
