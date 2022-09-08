<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%block name="title">${_('Parameter')} ${ctx.name}</%block>

<div style="margin-top: 30px;">
    <h2>${ctx.name}</h2>
    <p>
        ${ctx.description | n}
    </p>
    % if ctx.etyma:
    <h4>Etymological notes</h4>
    <p>${u.markdown_handle_links(request, ctx.etyma)|n}</p>
    % endif
</div>

<br>

<div style="clear: both; "/>

% if map_ or request.map:
${(map_ or request.map).render()}
% endif

${request.get_datatable('values', h.models.Value, parameter=ctx).render()}