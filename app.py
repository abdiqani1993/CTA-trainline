from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)

# Renders the home page
@app.route('/')
def home():
    return render_template('home.html')

# Buy a ticket page rendering
@app.route('/buy', methods=['GET', 'POST'])
def buy_ticket():
    if request.method == 'POST':
        # Gets form data
        name = request.form['name']
        depart = request.form['depart']
        destination = request.form['destination']
        ticket_type = request.form['ticket_type']
        zones = int(request.form['zones'])
        
        # Ticket prices per zone (in cents)
        prices = {
            'adult': 2105,
            'child': 1410,
            'senior': 1025,
            'student': 1750
        }
        
        # Calculate total price
        price_per_zone = prices.get(ticket_type, 0)
        total_price = price_per_zone * zones  # Total price in cents

        # Genarates a refrence number
        ticket_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        
        # Passes ticket info to the ticket.html template
        return render_template(
            'ticket.html',
            name=name,
            depart=depart,
            destination=destination,
            ticket_number=ticket_number,
            total_price=total_price /1000  # Convert cents to dollars
        )
    
    return render_template('buy_ticket.html')


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
