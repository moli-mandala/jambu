<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%block name="title">${_('Parameter')} ${ctx.name}</%block>


<div class="accordion-group" style="margin-top: 30px;">
    <div class="accordion-heading">
        <a class="accordion-toggle" data-toggle="collapse" data-parent="#meaning-more" href="#acc-a" title="click to hide or show IE-CoR Definition">       
            <h2>${ctx.name}</h2>
        </a>
    </div>
    <div id="acc-a" class="accordion-body collapse in">
        <div class="accordion-inner">
            ${ctx.description | n}
        </div>
        <div class="accordion-inner">
            Attested in ${ctx.count} lect(s).
        </div>
    </div>
</div>

<br>

<div style="clear: both; "/>

% if map_ or request.map:
${(map_ or request.map).render()}
% endif

${request.get_datatable('values', h.models.Value, parameter=ctx).render()}