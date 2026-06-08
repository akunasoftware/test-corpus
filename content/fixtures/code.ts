type AuditEvent = {
    readonly id: string;
    readonly kind: "created" | "reviewed" | "approved";
    readonly detail: string;
};

const events: AuditEvent[] = [
    { id: "evt-001", kind: "created", detail: "draft request opened" },
    { id: "evt-002", kind: "reviewed", detail: "extraction fixture marker: shared code sample" },
    { id: "evt-003", kind: "approved", detail: "manager approval recorded" },
];

function describeReviewEvents(auditEvents: readonly AuditEvent[]): string[] {
    return auditEvents
        .filter((event) => event.kind === "reviewed")
        .map((event) => `${event.id}: ${event.detail}`);
}

for (const description of describeReviewEvents(events)) {
    console.log(description);
}
