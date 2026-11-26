from components import render_html


def page_header(title, subtitle):
    render_html(
        f"""
        <div style="margin-bottom:28px;">
            <h1 style="color:white; font-size:34px;">
                {title}
            </h1>
            <p style="color:#aebbd8; font-size:16px;">
                {subtitle}
            </p>
        </div>
        """
    )