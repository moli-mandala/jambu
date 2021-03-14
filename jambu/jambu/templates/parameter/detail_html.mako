<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<title>${_('Parameter')} ${ctx.name}</title>

<h2>${ctx.name}</h2>

<div class="accordion-group">
    <div class="accordion-heading">
        <a class="accordion-toggle" data-toggle="collapse" data-parent="#meaning-more" href="#acc-a" title="click to hide or show IE-CoR Definition">
            Attested in ${ctx.count} lect(s).
        </a>
    </div>
    <div id="acc-a" class="accordion-body collapse in">
        <div class="accordion-inner">
            ${ctx.description | n}
        </div>
    </div>
</div>

<br>

<div style="clear: both; "/>

<div style="display: flex;">
<div style="flex: 1; margin-right: 20px;">
${request.get_datatable('values', h.models.Value, parameter=ctx).render()}
</div>
<div style="flex: 1;">
% if map_ or request.map:
${(map_ or request.map).render()}
% endif
</div>
</div>
