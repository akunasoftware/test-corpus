const shipments = [
    { id: "A-104", status: "packed", note: "labels printed" },
    { id: "B-208", status: "held", note: "extraction fixture marker: shared code sample" },
    { id: "C-319", status: "packed", note: "ready for dispatch" },
];

function summarizeHeldShipments(records) {
    return records
        .filter((record) => record.status === "held")
        .map((record) => `${record.id}: ${record.note}`);
}

for (const summary of summarizeHeldShipments(shipments)) {
    console.log(summary);
}
