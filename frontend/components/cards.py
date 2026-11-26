from components import render_html


def feature_card(icon, title, description):
    render_html(
        f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """
    )


def step_card(number, title, description):
    render_html(
        f"""
        <div class="step-card">
            <div class="step-number">{number}</div>
            <h4>{title}</h4>
            <p>{description}</p>
        </div>
        """
    )