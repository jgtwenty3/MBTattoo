import React, { useState } from 'react';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import 'react-big-calendar/lib/css/react-big-calendar.css';
import moment from 'moment';
import logo from "./logo.png";
import { NavLink } from "react-router-dom";
import Modal from 'react-modal';

const MyCalendar = () => {
  const localizer = momentLocalizer(moment);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [selectedEvent, setSelectedEvent] = useState(null);

  const handleEventClick = event => {
    setSelectedEvent(event);
    setModalIsOpen(true);
  };

  // Sample events data
  const events = [
    {
      title: 'Event 1',
      start: new Date(2024, 2, 20), // year, month (0-indexed), day
      end: new Date(2024, 2, 21),
      description: 'Details about Event 1',
    },
    {
      title: 'Event 2',
      start: new Date(2024, 2, 25),
      end: new Date(2024, 2, 26),
      description: 'Details about Event 2',
    },
  ];

  return (
    <div>
      <h2>
        <NavLink to="/">
          <img src={logo} className="App-logo-sm " alt="Fostr" />
        </NavLink>
        Shop Calendar
      </h2>
      <Calendar
        localizer={localizer}
        events={events}
        startAccessor="start"
        endAccessor="end"
        style={{ height: 500 }}
        onSelectEvent={handleEventClick}
      />
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={() => setModalIsOpen(false)}
      >
        {selectedEvent && (
          <div>
            <h2>{selectedEvent.title}</h2>
            <p>{selectedEvent.description}</p>
            <button onClick={() => setModalIsOpen(false)}>Close</button>
          </div>
        )}
      </Modal>
    </div>
  );
};

export default MyCalendar;
