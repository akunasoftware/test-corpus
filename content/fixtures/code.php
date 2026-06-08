<?php

declare(strict_types=1);

final class QueueEntry
{
    public function __construct(
        public readonly string $name,
        public readonly string $state,
        public readonly string $detail,
    ) {}
}

function describeEntry(QueueEntry $entry): string
{
    return sprintf('%s [%s]: %s', $entry->name, $entry->state, $entry->detail);
}

$entries = [
    new QueueEntry('parse', 'complete', 'front matter loaded'),
    new QueueEntry('extract', 'review', 'extraction fixture marker: shared code sample'),
    new QueueEntry('index', 'pending', 'search document queued'),
];

foreach ($entries as $entry) {
    echo describeEntry($entry) . PHP_EOL;
}
