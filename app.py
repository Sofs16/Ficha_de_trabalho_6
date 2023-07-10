from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RespostaForm, MensagemForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo'

respostas = ['pedro', '27', 'carlos']
mensagens = []


@app.route("/", methods=['GET', 'POST'])
def home():
    form = RespostaForm()
    return render_template('home.html', form=form)

@app.route("/desafio1", methods=['GET', 'POST'])
def desafio1():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[0]:
            return redirect(url_for('desafio2'))
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('desafio1.html', form=form)

@app.route("/desafio2", methods=['GET', 'POST'])
def desafio2():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[1]:
            return redirect(url_for('desafio3'))
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('desafio2.html', form=form)

@app.route("/desafio3", methods=['GET', 'POST'])
def desafio3():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[2]:
            return redirect(url_for('final'))
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('desafio3.html', form=form)

@app.route("/final", methods=['GET', 'POST'])

def final():
    form = MensagemForm()
    if form.validate_on_submit():
        mensagem = form.mensagem.data
        mensagens.append(mensagem)
        print(f'Mensagem recebida: {mensagem}') # Print da mensagem no terminal
        flash(f'Mensagem enviada com sucesso! Já existem {len(mensagens)} mensagem(s).', 'success')
    return render_template('tesouro.html', form=form)


@app.route("/mensagens")
def ver_mensagens():
    return render_template('mensagens.html', mensagens=mensagens)


if __name__ == "__main__":
    app.run()