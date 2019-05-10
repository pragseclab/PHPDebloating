<?php

/* export/alias_item.twig */
class __TwigTemplate_9e447929bbb76448519d37a5ca5c0a70c771e79dc5d648cb72165765eccf0a4b extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo "<tr>
    <th>";
        // line 2
        echo twig_escape_filter($this->env, (isset($context["type"]) ? $context["type"] : null), "html", null, true);
        echo "</th>
    <td>";
        // line 3
        echo twig_escape_filter($this->env, (isset($context["name"]) ? $context["name"] : null), "html", null, true);
        echo "</td>
    <td>
        <input name=\"";
        // line 5
        echo twig_escape_filter($this->env, (isset($context["field"]) ? $context["field"] : null), "html", null, true);
        echo "\" value=\"";
        echo twig_escape_filter($this->env, (isset($context["value"]) ? $context["value"] : null), "html", null, true);
        echo "\" type=\"text\" />
    </td>
    <td>
        <button class=\"alias_remove ui-button ui-corner-all ui-widget\">";
        // line 8
        echo _gettext("Remove");
        echo "</button>
    </td>
</tr>
";
    }

    public function getTemplateName()
    {
        return "export/alias_item.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  39 => 8,  31 => 5,  26 => 3,  22 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "export/alias_item.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/export/alias_item.twig");
    }
}
