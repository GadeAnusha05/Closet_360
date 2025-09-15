document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById('moodChart');

    if (ctx) {
        const moodData = JSON.parse(ctx.getAttribute('data-moods'));

        const dates = moodData.map(entry => entry.date);
        const sentiments = moodData.map(entry => entry.sentiment);

        new Chart(ctx, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Mood Sentiment Trend',
                    data: sentiments,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    fill: true,
                    tension: 0.3
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: true
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        min: -1,
                        max: 1,
                        title: {
                            display: true,
                            text: 'Sentiment'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Date'
                        }
                    }
                }
            }
        });
    }
});
